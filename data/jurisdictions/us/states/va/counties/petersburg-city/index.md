---
type: Jurisdiction
title: "Petersburg city, VA"
classification: county
fips: "51730"
state: "VA"
demographics:
  population: 33537
  population_under_18: 8545
  population_18_64: 11677
  population_65_plus: 13315
  median_household_income: 50698
  poverty_rate: 21.73
  homeownership_rate: 38.62
  unemployment_rate: 10.05
  median_home_value: 189000
  gini_index: 0.4361
  vacancy_rate: 16.25
  race_white: 5094
  race_black: 25663
  race_asian: 433
  race_native: 22
  hispanic: 2183
  bachelors_plus: 8086
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/13"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/va/districts/house/82"
    rel: in-district
    area_weight: 0.9984
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Petersburg city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33537 |
| Under 18 | 8545 |
| 18–64 | 11677 |
| 65+ | 13315 |
| Median household income | 50698 |
| Poverty rate | 21.73 |
| Homeownership rate | 38.62 |
| Unemployment rate | 10.05 |
| Median home value | 189000 |
| Gini index | 0.4361 |
| Vacancy rate | 16.25 |
| White | 5094 |
| Black | 25663 |
| Asian | 433 |
| Native | 22 |
| Hispanic/Latino | 2183 |
| Bachelor's or higher | 8086 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 100% (congressional)
- [VA Senate District 13](/us/states/va/districts/senate/13.md) — 100% (state senate)
- [VA House District 82](/us/states/va/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
