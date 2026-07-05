---
type: Jurisdiction
title: "Middlesex County, VA"
classification: county
fips: "51119"
state: "VA"
demographics:
  population: 10847
  population_under_18: 1740
  population_18_64: 5403
  population_65_plus: 3704
  median_household_income: 75060
  poverty_rate: 7.31
  homeownership_rate: 87.43
  unemployment_rate: 2.88
  median_home_value: 352200
  gini_index: 0.4102
  vacancy_rate: 33.29
  race_white: 8556
  race_black: 1747
  race_asian: 43
  race_native: 6
  hispanic: 349
  bachelors_plus: 3913
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.6705
  - to: "us/states/va/districts/senate/25"
    rel: in-district
    area_weight: 0.6618
  - to: "us/states/va/districts/house/68"
    rel: in-district
    area_weight: 0.6622
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Middlesex County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10847 |
| Under 18 | 1740 |
| 18–64 | 5403 |
| 65+ | 3704 |
| Median household income | 75060 |
| Poverty rate | 7.31 |
| Homeownership rate | 87.43 |
| Unemployment rate | 2.88 |
| Median home value | 352200 |
| Gini index | 0.4102 |
| Vacancy rate | 33.29 |
| White | 8556 |
| Black | 1747 |
| Asian | 43 |
| Native | 6 |
| Hispanic/Latino | 349 |
| Bachelor's or higher | 3913 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 67% (congressional)
- [VA Senate District 25](/us/states/va/districts/senate/25.md) — 66% (state senate)
- [VA House District 68](/us/states/va/districts/house/68.md) — 66% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
