---
type: Jurisdiction
title: "Hood County, TX"
classification: county
fips: "48221"
state: "TX"
demographics:
  population: 65894
  population_under_18: 13467
  population_18_64: 35587
  population_65_plus: 16840
  median_household_income: 88160
  poverty_rate: 7.66
  homeownership_rate: 81.17
  unemployment_rate: 5.63
  median_home_value: 306400
  gini_index: 0.4435
  vacancy_rate: 12.19
  race_white: 55776
  race_black: 737
  race_asian: 520
  race_native: 275
  hispanic: 9069
  bachelors_plus: 20734
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/22"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/59"
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

# Hood County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65894 |
| Under 18 | 13467 |
| 18–64 | 35587 |
| 65+ | 16840 |
| Median household income | 88160 |
| Poverty rate | 7.66 |
| Homeownership rate | 81.17 |
| Unemployment rate | 5.63 |
| Median home value | 306400 |
| Gini index | 0.4435 |
| Vacancy rate | 12.19 |
| White | 55776 |
| Black | 737 |
| Asian | 520 |
| Native | 275 |
| Hispanic/Latino | 9069 |
| Bachelor's or higher | 20734 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 100% (congressional)
- [TX Senate District 22](/us/states/tx/districts/senate/22.md) — 100% (state senate)
- [TX House District 59](/us/states/tx/districts/house/59.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
