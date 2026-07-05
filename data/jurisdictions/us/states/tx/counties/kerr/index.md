---
type: Jurisdiction
title: "Kerr County, TX"
classification: county
fips: "48265"
state: "TX"
demographics:
  population: 53489
  population_under_18: 9675
  population_18_64: 28270
  population_65_plus: 15544
  median_household_income: 69395
  poverty_rate: 11.36
  homeownership_rate: 70.14
  unemployment_rate: 3.29
  median_home_value: 321200
  gini_index: 0.4556
  vacancy_rate: 11.77
  race_white: 39539
  race_black: 850
  race_asian: 618
  race_native: 368
  hispanic: 14337
  bachelors_plus: 17218
districts:
  - to: "us/states/tx/districts/21"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/53"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Kerr County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53489 |
| Under 18 | 9675 |
| 18–64 | 28270 |
| 65+ | 15544 |
| Median household income | 69395 |
| Poverty rate | 11.36 |
| Homeownership rate | 70.14 |
| Unemployment rate | 3.29 |
| Median home value | 321200 |
| Gini index | 0.4556 |
| Vacancy rate | 11.77 |
| White | 39539 |
| Black | 850 |
| Asian | 618 |
| Native | 368 |
| Hispanic/Latino | 14337 |
| Bachelor's or higher | 17218 |

## Districts

- [TX-21](/us/states/tx/districts/21.md) — 100% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
