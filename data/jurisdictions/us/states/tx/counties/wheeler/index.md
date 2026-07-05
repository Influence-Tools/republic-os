---
type: Jurisdiction
title: "Wheeler County, TX"
classification: county
fips: "48483"
state: "TX"
demographics:
  population: 4862
  population_under_18: 1177
  population_18_64: 2680
  population_65_plus: 1005
  median_household_income: 60167
  poverty_rate: 15.4
  homeownership_rate: 76.24
  unemployment_rate: 4.76
  median_home_value: 106100
  gini_index: 0.4184
  vacancy_rate: 26.02
  race_white: 3929
  race_black: 69
  race_asian: 56
  race_native: 82
  hispanic: 1233
  bachelors_plus: 682
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/house/88"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Wheeler County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4862 |
| Under 18 | 1177 |
| 18–64 | 2680 |
| 65+ | 1005 |
| Median household income | 60167 |
| Poverty rate | 15.4 |
| Homeownership rate | 76.24 |
| Unemployment rate | 4.76 |
| Median home value | 106100 |
| Gini index | 0.4184 |
| Vacancy rate | 26.02 |
| White | 3929 |
| Black | 69 |
| Asian | 56 |
| Native | 82 |
| Hispanic/Latino | 1233 |
| Bachelor's or higher | 682 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
