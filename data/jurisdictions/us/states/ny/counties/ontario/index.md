---
type: Jurisdiction
title: "Ontario County, NY"
classification: county
fips: "36069"
state: "NY"
demographics:
  population: 112625
  population_under_18: 21668
  population_18_64: 65994
  population_65_plus: 24963
  median_household_income: 82324
  poverty_rate: 9.01
  homeownership_rate: 73.69
  unemployment_rate: 3.71
  median_home_value: 222900
  gini_index: 0.4417
  vacancy_rate: 9.49
  race_white: 99659
  race_black: 2353
  race_asian: 1578
  race_native: 34
  hispanic: 6438
  bachelors_plus: 44723
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.923
  - to: "us/states/ny/districts/25"
    rel: in-district
    area_weight: 0.077
  - to: "us/states/ny/districts/senate/54"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/house/131"
    rel: in-district
    area_weight: 0.5029
  - to: "us/states/ny/districts/house/133"
    rel: in-district
    area_weight: 0.4969
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Ontario County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 112625 |
| Under 18 | 21668 |
| 18–64 | 65994 |
| 65+ | 24963 |
| Median household income | 82324 |
| Poverty rate | 9.01 |
| Homeownership rate | 73.69 |
| Unemployment rate | 3.71 |
| Median home value | 222900 |
| Gini index | 0.4417 |
| Vacancy rate | 9.49 |
| White | 99659 |
| Black | 2353 |
| Asian | 1578 |
| Native | 34 |
| Hispanic/Latino | 6438 |
| Bachelor's or higher | 44723 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 92% (congressional)
- [NY-25](/us/states/ny/districts/25.md) — 8% (congressional)
- [NY Senate District 54](/us/states/ny/districts/senate/54.md) — 100% (state senate)
- [NY House District 131](/us/states/ny/districts/house/131.md) — 50% (state house)
- [NY House District 133](/us/states/ny/districts/house/133.md) — 50% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
