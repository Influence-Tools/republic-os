---
type: Jurisdiction
title: "Buchanan County, IA"
classification: county
fips: "19019"
state: "IA"
demographics:
  population: 20694
  population_under_18: 5251
  population_18_64: 11588
  population_65_plus: 3855
  median_household_income: 78236
  poverty_rate: 8.6
  homeownership_rate: 82.13
  unemployment_rate: 2.84
  median_home_value: 176000
  gini_index: 0.3852
  vacancy_rate: 7.75
  race_white: 19862
  race_black: 124
  race_asian: 40
  race_native: 58
  hispanic: 400
  bachelors_plus: 3929
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/34"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/67"
    rel: in-district
    area_weight: 0.5594
  - to: "us/states/ia/districts/house/68"
    rel: in-district
    area_weight: 0.4405
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Buchanan County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20694 |
| Under 18 | 5251 |
| 18–64 | 11588 |
| 65+ | 3855 |
| Median household income | 78236 |
| Poverty rate | 8.6 |
| Homeownership rate | 82.13 |
| Unemployment rate | 2.84 |
| Median home value | 176000 |
| Gini index | 0.3852 |
| Vacancy rate | 7.75 |
| White | 19862 |
| Black | 124 |
| Asian | 40 |
| Native | 58 |
| Hispanic/Latino | 400 |
| Bachelor's or higher | 3929 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 34](/us/states/ia/districts/senate/34.md) — 100% (state senate)
- [IA House District 67](/us/states/ia/districts/house/67.md) — 56% (state house)
- [IA House District 68](/us/states/ia/districts/house/68.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
