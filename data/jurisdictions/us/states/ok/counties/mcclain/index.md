---
type: Jurisdiction
title: "McClain County, OK"
classification: county
fips: "40087"
state: "OK"
demographics:
  population: 45273
  population_under_18: 11357
  population_18_64: 26862
  population_65_plus: 7054
  median_household_income: 84552
  poverty_rate: 8.52
  homeownership_rate: 79.29
  unemployment_rate: 4.7
  median_home_value: 255900
  gini_index: 0.4299
  vacancy_rate: 6.86
  race_white: 35192
  race_black: 550
  race_asian: 269
  race_native: 2597
  hispanic: 4414
  bachelors_plus: 11274
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ok/districts/senate/43"
    rel: in-district
    area_weight: 0.8217
  - to: "us/states/ok/districts/senate/13"
    rel: in-district
    area_weight: 0.1782
  - to: "us/states/ok/districts/house/42"
    rel: in-district
    area_weight: 0.62
  - to: "us/states/ok/districts/house/20"
    rel: in-district
    area_weight: 0.2923
  - to: "us/states/ok/districts/house/25"
    rel: in-district
    area_weight: 0.0876
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# McClain County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45273 |
| Under 18 | 11357 |
| 18–64 | 26862 |
| 65+ | 7054 |
| Median household income | 84552 |
| Poverty rate | 8.52 |
| Homeownership rate | 79.29 |
| Unemployment rate | 4.7 |
| Median home value | 255900 |
| Gini index | 0.4299 |
| Vacancy rate | 6.86 |
| White | 35192 |
| Black | 550 |
| Asian | 269 |
| Native | 2597 |
| Hispanic/Latino | 4414 |
| Bachelor's or higher | 11274 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 43](/us/states/ok/districts/senate/43.md) — 82% (state senate)
- [OK Senate District 13](/us/states/ok/districts/senate/13.md) — 18% (state senate)
- [OK House District 42](/us/states/ok/districts/house/42.md) — 62% (state house)
- [OK House District 20](/us/states/ok/districts/house/20.md) — 29% (state house)
- [OK House District 25](/us/states/ok/districts/house/25.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
