---
type: Jurisdiction
title: "Worth County, IA"
classification: county
fips: "19195"
state: "IA"
demographics:
  population: 7350
  population_under_18: 1520
  population_18_64: 4146
  population_65_plus: 1684
  median_household_income: 78008
  poverty_rate: 8.17
  homeownership_rate: 83.2
  unemployment_rate: 3.55
  median_home_value: 145800
  gini_index: 0.3981
  vacancy_rate: 8.52
  race_white: 6956
  race_black: 59
  race_asian: 41
  race_native: 12
  hispanic: 258
  bachelors_plus: 1275
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ia/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/60"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Worth County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7350 |
| Under 18 | 1520 |
| 18–64 | 4146 |
| 65+ | 1684 |
| Median household income | 78008 |
| Poverty rate | 8.17 |
| Homeownership rate | 83.2 |
| Unemployment rate | 3.55 |
| Median home value | 145800 |
| Gini index | 0.3981 |
| Vacancy rate | 8.52 |
| White | 6956 |
| Black | 59 |
| Asian | 41 |
| Native | 12 |
| Hispanic/Latino | 258 |
| Bachelor's or higher | 1275 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 30](/us/states/ia/districts/senate/30.md) — 100% (state senate)
- [IA House District 60](/us/states/ia/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
