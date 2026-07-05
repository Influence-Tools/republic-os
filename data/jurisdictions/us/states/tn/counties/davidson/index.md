---
type: Jurisdiction
title: "Davidson County, TN"
classification: county
fips: "47037"
state: "TN"
demographics:
  population: 715388
  population_under_18: 166762
  population_18_64: 299964
  population_65_plus: 248662
  median_household_income: 77853
  poverty_rate: 13.95
  homeownership_rate: 52.79
  unemployment_rate: 4.49
  median_home_value: 417400
  gini_index: 0.4927
  vacancy_rate: 9.02
  race_white: 395172
  race_black: 175808
  race_asian: 24838
  race_native: 3571
  hispanic: 99569
  bachelors_plus: 333908
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.4002
  - to: "us/states/tn/districts/05"
    rel: in-district
    area_weight: 0.3771
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.2217
  - to: "us/states/tn/districts/senate/20"
    rel: in-district
    area_weight: 0.5368
  - to: "us/states/tn/districts/senate/19"
    rel: in-district
    area_weight: 0.2267
  - to: "us/states/tn/districts/senate/21"
    rel: in-district
    area_weight: 0.1187
  - to: "us/states/tn/districts/senate/17"
    rel: in-district
    area_weight: 0.1174
  - to: "us/states/tn/districts/house/50"
    rel: in-district
    area_weight: 0.3108
  - to: "us/states/tn/districts/house/59"
    rel: in-district
    area_weight: 0.1504
  - to: "us/states/tn/districts/house/54"
    rel: in-district
    area_weight: 0.1178
  - to: "us/states/tn/districts/house/52"
    rel: in-district
    area_weight: 0.1088
  - to: "us/states/tn/districts/house/60"
    rel: in-district
    area_weight: 0.0888
  - to: "us/states/tn/districts/house/51"
    rel: in-district
    area_weight: 0.0679
  - to: "us/states/tn/districts/house/53"
    rel: in-district
    area_weight: 0.052
  - to: "us/states/tn/districts/house/58"
    rel: in-district
    area_weight: 0.0376
  - to: "us/states/tn/districts/house/55"
    rel: in-district
    area_weight: 0.0347
  - to: "us/states/tn/districts/house/56"
    rel: in-district
    area_weight: 0.0307
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Davidson County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 715388 |
| Under 18 | 166762 |
| 18–64 | 299964 |
| 65+ | 248662 |
| Median household income | 77853 |
| Poverty rate | 13.95 |
| Homeownership rate | 52.79 |
| Unemployment rate | 4.49 |
| Median home value | 417400 |
| Gini index | 0.4927 |
| Vacancy rate | 9.02 |
| White | 395172 |
| Black | 175808 |
| Asian | 24838 |
| Native | 3571 |
| Hispanic/Latino | 99569 |
| Bachelor's or higher | 333908 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 40% (congressional)
- [TN-05](/us/states/tn/districts/05.md) — 38% (congressional)
- [TN-06](/us/states/tn/districts/06.md) — 22% (congressional)
- [TN Senate District 20](/us/states/tn/districts/senate/20.md) — 54% (state senate)
- [TN Senate District 19](/us/states/tn/districts/senate/19.md) — 23% (state senate)
- [TN Senate District 21](/us/states/tn/districts/senate/21.md) — 12% (state senate)
- [TN Senate District 17](/us/states/tn/districts/senate/17.md) — 12% (state senate)
- [TN House District 50](/us/states/tn/districts/house/50.md) — 31% (state house)
- [TN House District 59](/us/states/tn/districts/house/59.md) — 15% (state house)
- [TN House District 54](/us/states/tn/districts/house/54.md) — 12% (state house)
- [TN House District 52](/us/states/tn/districts/house/52.md) — 11% (state house)
- [TN House District 60](/us/states/tn/districts/house/60.md) — 9% (state house)
- [TN House District 51](/us/states/tn/districts/house/51.md) — 7% (state house)
- [TN House District 53](/us/states/tn/districts/house/53.md) — 5% (state house)
- [TN House District 58](/us/states/tn/districts/house/58.md) — 4% (state house)
- [TN House District 55](/us/states/tn/districts/house/55.md) — 3% (state house)
- [TN House District 56](/us/states/tn/districts/house/56.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
