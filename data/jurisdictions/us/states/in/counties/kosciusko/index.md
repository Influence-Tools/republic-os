---
type: Jurisdiction
title: "Kosciusko County, IN"
classification: county
fips: "18085"
state: "IN"
demographics:
  population: 80442
  population_under_18: 18929
  population_18_64: 46972
  population_65_plus: 14541
  median_household_income: 75317
  poverty_rate: 9.85
  homeownership_rate: 76.98
  unemployment_rate: 2.77
  median_home_value: 216000
  gini_index: 0.4048
  vacancy_rate: 17.83
  race_white: 69905
  race_black: 472
  race_asian: 1119
  race_native: 30
  hispanic: 7818
  bachelors_plus: 18146
districts:
  - to: "us/states/in/districts/02"
    rel: in-district
    area_weight: 0.8082
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.1918
  - to: "us/states/in/districts/senate/18"
    rel: in-district
    area_weight: 0.5041
  - to: "us/states/in/districts/senate/9"
    rel: in-district
    area_weight: 0.4958
  - to: "us/states/in/districts/house/22"
    rel: in-district
    area_weight: 0.8726
  - to: "us/states/in/districts/house/18"
    rel: in-district
    area_weight: 0.1274
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Kosciusko County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 80442 |
| Under 18 | 18929 |
| 18–64 | 46972 |
| 65+ | 14541 |
| Median household income | 75317 |
| Poverty rate | 9.85 |
| Homeownership rate | 76.98 |
| Unemployment rate | 2.77 |
| Median home value | 216000 |
| Gini index | 0.4048 |
| Vacancy rate | 17.83 |
| White | 69905 |
| Black | 472 |
| Asian | 1119 |
| Native | 30 |
| Hispanic/Latino | 7818 |
| Bachelor's or higher | 18146 |

## Districts

- [IN-02](/us/states/in/districts/02.md) — 81% (congressional)
- [IN-03](/us/states/in/districts/03.md) — 19% (congressional)
- [IN Senate District 18](/us/states/in/districts/senate/18.md) — 50% (state senate)
- [IN Senate District 9](/us/states/in/districts/senate/9.md) — 50% (state senate)
- [IN House District 22](/us/states/in/districts/house/22.md) — 87% (state house)
- [IN House District 18](/us/states/in/districts/house/18.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
