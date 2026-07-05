---
type: Jurisdiction
title: "Clay County, WV"
classification: county
fips: "54015"
state: "WV"
demographics:
  population: 7835
  population_under_18: 1708
  population_18_64: 4369
  population_65_plus: 1758
  median_household_income: 42318
  poverty_rate: 26.43
  homeownership_rate: 75.98
  unemployment_rate: 11.86
  median_home_value: 109100
  gini_index: 0.4773
  vacancy_rate: 24.97
  race_white: 7587
  race_black: 4
  race_asian: 0
  race_native: 4
  hispanic: 18
  bachelors_plus: 854
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/8"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/62"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Clay County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7835 |
| Under 18 | 1708 |
| 18–64 | 4369 |
| 65+ | 1758 |
| Median household income | 42318 |
| Poverty rate | 26.43 |
| Homeownership rate | 75.98 |
| Unemployment rate | 11.86 |
| Median home value | 109100 |
| Gini index | 0.4773 |
| Vacancy rate | 24.97 |
| White | 7587 |
| Black | 4 |
| Asian | 0 |
| Native | 4 |
| Hispanic/Latino | 18 |
| Bachelor's or higher | 854 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 8](/us/states/wv/districts/senate/8.md) — 100% (state senate)
- [WV House District 62](/us/states/wv/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
