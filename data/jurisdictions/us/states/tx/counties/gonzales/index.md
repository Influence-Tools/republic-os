---
type: Jurisdiction
title: "Gonzales County, TX"
classification: county
fips: "48177"
state: "TX"
demographics:
  population: 19851
  population_under_18: 5056
  population_18_64: 11199
  population_65_plus: 3596
  median_household_income: 58672
  poverty_rate: 15.82
  homeownership_rate: 66.21
  unemployment_rate: 4.31
  median_home_value: 159100
  gini_index: 0.4618
  vacancy_rate: 12.13
  race_white: 10687
  race_black: 1281
  race_asian: 84
  race_native: 244
  hispanic: 10139
  bachelors_plus: 1974
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/44"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Gonzales County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19851 |
| Under 18 | 5056 |
| 18–64 | 11199 |
| 65+ | 3596 |
| Median household income | 58672 |
| Poverty rate | 15.82 |
| Homeownership rate | 66.21 |
| Unemployment rate | 4.31 |
| Median home value | 159100 |
| Gini index | 0.4618 |
| Vacancy rate | 12.13 |
| White | 10687 |
| Black | 1281 |
| Asian | 84 |
| Native | 244 |
| Hispanic/Latino | 10139 |
| Bachelor's or higher | 1974 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 100% (state senate)
- [TX House District 44](/us/states/tx/districts/house/44.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
