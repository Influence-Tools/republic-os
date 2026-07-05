---
type: Jurisdiction
title: "Essex County, NY"
classification: county
fips: "36031"
state: "NY"
demographics:
  population: 36973
  population_under_18: 5703
  population_18_64: 21513
  population_65_plus: 9757
  median_household_income: 71661
  poverty_rate: 11.21
  homeownership_rate: 77.25
  unemployment_rate: 3.97
  median_home_value: 211900
  gini_index: 0.4545
  vacancy_rate: 35.87
  race_white: 34284
  race_black: 817
  race_asian: 234
  race_native: 59
  hispanic: 1059
  bachelors_plus: 13818
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/senate/45"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/114"
    rel: in-district
    area_weight: 0.7361
  - to: "us/states/ny/districts/house/115"
    rel: in-district
    area_weight: 0.2638
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Essex County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36973 |
| Under 18 | 5703 |
| 18–64 | 21513 |
| 65+ | 9757 |
| Median household income | 71661 |
| Poverty rate | 11.21 |
| Homeownership rate | 77.25 |
| Unemployment rate | 3.97 |
| Median home value | 211900 |
| Gini index | 0.4545 |
| Vacancy rate | 35.87 |
| White | 34284 |
| Black | 817 |
| Asian | 234 |
| Native | 59 |
| Hispanic/Latino | 1059 |
| Bachelor's or higher | 13818 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 45](/us/states/ny/districts/senate/45.md) — 100% (state senate)
- [NY House District 114](/us/states/ny/districts/house/114.md) — 74% (state house)
- [NY House District 115](/us/states/ny/districts/house/115.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
