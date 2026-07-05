---
type: Jurisdiction
title: "Greene County, VA"
classification: county
fips: "51079"
state: "VA"
demographics:
  population: 21155
  population_under_18: 4850
  population_18_64: 12178
  population_65_plus: 4127
  median_household_income: 89808
  poverty_rate: 13.74
  homeownership_rate: 83.42
  unemployment_rate: 1.81
  median_home_value: 343300
  gini_index: 0.4282
  vacancy_rate: 9.26
  race_white: 16708
  race_black: 1563
  race_asian: 464
  race_native: 8
  hispanic: 1578
  bachelors_plus: 6475
districts:
  - to: "us/states/va/districts/07"
    rel: in-district
    area_weight: 0.9884
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.0098
  - to: "us/states/va/districts/senate/28"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/va/districts/house/62"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Greene County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21155 |
| Under 18 | 4850 |
| 18–64 | 12178 |
| 65+ | 4127 |
| Median household income | 89808 |
| Poverty rate | 13.74 |
| Homeownership rate | 83.42 |
| Unemployment rate | 1.81 |
| Median home value | 343300 |
| Gini index | 0.4282 |
| Vacancy rate | 9.26 |
| White | 16708 |
| Black | 1563 |
| Asian | 464 |
| Native | 8 |
| Hispanic/Latino | 1578 |
| Bachelor's or higher | 6475 |

## Districts

- [VA-07](/us/states/va/districts/07.md) — 99% (congressional)
- [VA-06](/us/states/va/districts/06.md) — 1% (congressional)
- [VA Senate District 28](/us/states/va/districts/senate/28.md) — 100% (state senate)
- [VA House District 62](/us/states/va/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
