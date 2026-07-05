---
type: Jurisdiction
title: "Cumberland County, NC"
classification: county
fips: "37051"
state: "NC"
demographics:
  population: 338545
  population_under_18: 85028
  population_18_64: 209486
  population_65_plus: 44031
  median_household_income: 61291
  poverty_rate: 16.7
  homeownership_rate: 54.97
  unemployment_rate: 7.64
  median_home_value: 199200
  gini_index: 0.4485
  vacancy_rate: 9.76
  race_white: 143594
  race_black: 127504
  race_asian: 9026
  race_native: 4103
  hispanic: 42995
  bachelors_plus: 79839
districts:
  - to: "us/states/nc/districts/07"
    rel: in-district
    area_weight: 0.7952
  - to: "us/states/nc/districts/09"
    rel: in-district
    area_weight: 0.2037
  - to: "us/states/nc/districts/senate/21"
    rel: in-district
    area_weight: 0.8052
  - to: "us/states/nc/districts/senate/19"
    rel: in-district
    area_weight: 0.1943
  - to: "us/states/nc/districts/house/43"
    rel: in-district
    area_weight: 0.7005
  - to: "us/states/nc/districts/house/42"
    rel: in-district
    area_weight: 0.1581
  - to: "us/states/nc/districts/house/45"
    rel: in-district
    area_weight: 0.0772
  - to: "us/states/nc/districts/house/44"
    rel: in-district
    area_weight: 0.0637
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Cumberland County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 338545 |
| Under 18 | 85028 |
| 18–64 | 209486 |
| 65+ | 44031 |
| Median household income | 61291 |
| Poverty rate | 16.7 |
| Homeownership rate | 54.97 |
| Unemployment rate | 7.64 |
| Median home value | 199200 |
| Gini index | 0.4485 |
| Vacancy rate | 9.76 |
| White | 143594 |
| Black | 127504 |
| Asian | 9026 |
| Native | 4103 |
| Hispanic/Latino | 42995 |
| Bachelor's or higher | 79839 |

## Districts

- [NC-07](/us/states/nc/districts/07.md) — 80% (congressional)
- [NC-09](/us/states/nc/districts/09.md) — 20% (congressional)
- [NC Senate District 21](/us/states/nc/districts/senate/21.md) — 81% (state senate)
- [NC Senate District 19](/us/states/nc/districts/senate/19.md) — 19% (state senate)
- [NC House District 43](/us/states/nc/districts/house/43.md) — 70% (state house)
- [NC House District 42](/us/states/nc/districts/house/42.md) — 16% (state house)
- [NC House District 45](/us/states/nc/districts/house/45.md) — 8% (state house)
- [NC House District 44](/us/states/nc/districts/house/44.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
