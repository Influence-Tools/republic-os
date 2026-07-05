---
type: Jurisdiction
title: "Hampton city, VA"
classification: county
fips: "51650"
state: "VA"
demographics:
  population: 137557
  population_under_18: 33579
  population_18_64: 49481
  population_65_plus: 54497
  median_household_income: 69621
  poverty_rate: 12.72
  homeownership_rate: 56.92
  unemployment_rate: 6.34
  median_home_value: 245700
  gini_index: 0.4337
  vacancy_rate: 7.24
  race_white: 50457
  race_black: 67805
  race_asian: 3131
  race_native: 418
  hispanic: 9447
  bachelors_plus: 36966
districts:
  - to: "us/states/va/districts/03"
    rel: in-district
    area_weight: 0.4269
  - to: "us/states/va/districts/senate/23"
    rel: in-district
    area_weight: 0.4294
  - to: "us/states/va/districts/house/87"
    rel: in-district
    area_weight: 0.2153
  - to: "us/states/va/districts/house/86"
    rel: in-district
    area_weight: 0.2142
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Hampton city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 137557 |
| Under 18 | 33579 |
| 18–64 | 49481 |
| 65+ | 54497 |
| Median household income | 69621 |
| Poverty rate | 12.72 |
| Homeownership rate | 56.92 |
| Unemployment rate | 6.34 |
| Median home value | 245700 |
| Gini index | 0.4337 |
| Vacancy rate | 7.24 |
| White | 50457 |
| Black | 67805 |
| Asian | 3131 |
| Native | 418 |
| Hispanic/Latino | 9447 |
| Bachelor's or higher | 36966 |

## Districts

- [VA-03](/us/states/va/districts/03.md) — 43% (congressional)
- [VA Senate District 23](/us/states/va/districts/senate/23.md) — 43% (state senate)
- [VA House District 87](/us/states/va/districts/house/87.md) — 22% (state house)
- [VA House District 86](/us/states/va/districts/house/86.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
