---
type: Jurisdiction
title: "Herkimer County, NY"
classification: county
fips: "36043"
state: "NY"
demographics:
  population: 59757
  population_under_18: 12183
  population_18_64: 34256
  population_65_plus: 13318
  median_household_income: 68515
  poverty_rate: 13.41
  homeownership_rate: 76.62
  unemployment_rate: 4.33
  median_home_value: 147700
  gini_index: 0.4416
  vacancy_rate: 20.7
  race_white: 54844
  race_black: 751
  race_asian: 369
  race_native: 45
  hispanic: 1700
  bachelors_plus: 13792
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ny/districts/senate/49"
    rel: in-district
    area_weight: 0.9394
  - to: "us/states/ny/districts/senate/53"
    rel: in-district
    area_weight: 0.0605
  - to: "us/states/ny/districts/house/118"
    rel: in-district
    area_weight: 0.9633
  - to: "us/states/ny/districts/house/122"
    rel: in-district
    area_weight: 0.0366
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Herkimer County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59757 |
| Under 18 | 12183 |
| 18–64 | 34256 |
| 65+ | 13318 |
| Median household income | 68515 |
| Poverty rate | 13.41 |
| Homeownership rate | 76.62 |
| Unemployment rate | 4.33 |
| Median home value | 147700 |
| Gini index | 0.4416 |
| Vacancy rate | 20.7 |
| White | 54844 |
| Black | 751 |
| Asian | 369 |
| Native | 45 |
| Hispanic/Latino | 1700 |
| Bachelor's or higher | 13792 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 49](/us/states/ny/districts/senate/49.md) — 94% (state senate)
- [NY Senate District 53](/us/states/ny/districts/senate/53.md) — 6% (state senate)
- [NY House District 118](/us/states/ny/districts/house/118.md) — 96% (state house)
- [NY House District 122](/us/states/ny/districts/house/122.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
